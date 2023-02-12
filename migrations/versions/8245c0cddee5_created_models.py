"""created models

Revision ID: 8245c0cddee5
Revises: 
Create Date: 2023-02-12 18:45:39.388216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8245c0cddee5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reflex',
    sa.Column('reflex_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('videos', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('education', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('reflex_id')
    )
    op.create_table('diary',
    sa.Column('diary_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('entry', sa.String(), nullable=False),
    sa.Column('posted_at', sa.DateTime(), nullable=False),
    sa.Column('reflex_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['reflex_id'], ['reflex.reflex_id'], ),
    sa.PrimaryKeyConstraint('diary_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('diary')
    op.drop_table('reflex')
    # ### end Alembic commands ###
