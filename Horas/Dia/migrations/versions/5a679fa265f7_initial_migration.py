"""initial migration

Revision ID: 5a679fa265f7
Revises: 
Create Date: 2024-02-05 20:36:17.092530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a679fa265f7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('registro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(length=19), nullable=False),
    sa.Column('entrada_manha', sa.String(length=5), nullable=False),
    sa.Column('saida_almoco', sa.String(length=5), nullable=False),
    sa.Column('entrada_tarde', sa.String(length=5), nullable=False),
    sa.Column('saida_noite', sa.String(length=5), nullable=False),
    sa.Column('total_horas', sa.String(length=5), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('registro')
    # ### end Alembic commands ###
